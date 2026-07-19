# VarshaDanduri.github.io
Varsha Danduri's portfolio


# Anika rig
The Anika rig is a free-rig I created to test and build upon the character creation process, including both artistic aspects (design, modelling) as well as more technical parts (rigging, shaders).

[add lead-character-turnaround]
Sketch of Anika 

I had originally designed for a short film I created, and started with a sketch. After a turnaround sketch, I began poly-modelling the character. Here I made sure to keep in mind edge flow for deformations, and keeping in context the poles and the density of quads. 

[add topology]
Wireframe of Anika

After that modelling the character, I began texturing. I added seams to the character, and made the UV. Since I wanted to go for a more hand painted look, I started normal-painting. I generated a normal map of the character, and started painting the direction of the normal in Krita. I think hooked up the new normal paint to the BSDF of the character. 

[add New_Normal_Body]
Painted Normal map with UVs

I began now to texture the hair. I created a custom shader which used the y-axis of the UV. Using a perline noise node, I could create differentiating lines on the UV. I used a color-ramp to generate a band around the middle of the hair. That band follows the camera direction to have the location shift higher when the camera is higher and lower when the camera is lower. Then I added a color mix, to use the colors of the hair and change the highlighting. I passed this into a BSDF node to then have the highlight be interactive with the lighting, and change hue based off it. 

[show a progression with uv-hair -> band-hair -> final-hair]
Shader hair progress

After that I wanted to create a fun looking silk texture for Anika dress. I wanted to create a painted looking, so for that I used the meshes normal, and plugged that in as a vector for a Voronoi texture. The texture allows broad bands of color on parts of the mesh that does not change in height much, and more bands of complex places of the mesh. After that, I then used the reflection of the mesh, and applied a color ramp to make the more reflective parts metallic. I thought this through because of the way silk, specificallly *italics* retained sericin has a more metallic look. After that, I added a color mix node to make the darker parts of the color to have a blue-ish tint, to make it colorful to look at. 

[show silk-shader]
Silk shading for the dress

Finally was rigging. I used a rig that included shapekeys, both as corrective, and to make different parts of the facial expressions. This was used for the body and the face. The rig controls were chosen to be intuitive to the animator. Another part was the cutom rig I made for Anika's skirt. I created a pseudo-collision detection with the bones, that would only deform if the bones moved past a certain rotation. This then affected the mesh. I used both detection bones, as well as skirt bones to create a smoother curve when the mesh moved. 

[add rigged-character]
[add skirt-bone-rig]
Rigged face and video of skirt rigging

And with that Anika model is complete, both a learning expeirence for me, as well as a free rig. 
[add rendered character]


# Grass Shader
A Unity URP grass system — one compute thread per source triangle, append buffer, single indirect draw.

https://github.com/VarshaDanduri/procedural-grass-unity/tree/main/Shader

Explain: blade sections built as stacked square segments → triangles from adjacent vertex triplets; rotation via bend/twist/wind matrices (wind scales with height v); gradientNoise for wind strength affecting AngleAxis3x3; fragment darkens albedo by windStrength and blends shadow tint; ProceduralGrassRenderer.cs dispatches compute + DrawProceduralIndirect; ProceduralGrassRendererEditor.cs custom inspector + tileable Perlin wind texture generator.

[add grass-image]
Procedural grass in scene

[add perlin-noise]
Wind moving through the field

[add tool-use]
Adjusting grass and wind in the Unity inspector


# Bouncing Ball
OpenGL simulation parallelizing multiple ball collisions on the GPU. State stored as (x, y, vx, vy) in a 1×N RGBA32F texture, ping-ponged each frame. physics.frag.glsl: one fragment per ball, collision via conservation of momentum along normal, wall bounce, damping, integration. render.vert/frag.glsl: instanced draw with gl_InstanceID, circle clip, per-ball color hash.

https://github.com/VarshaDanduri/bouncing-ball

[add bouncing-ball-video]
Multiple balls colliding in parallel


# Metal Shader
A procedural metal material in Blender — water droplets on a weathered steel surface, built layer by layer from noise textures through normal mapping to a metallic BSDF.

[add rigged-multifractal]
Musgrave multifractal mapped onto the sphere

I started with a Musgrave texture set to multifractal mode, mapped onto the sphere's surface coordinates. This gave a base layer of organic variation — streaky, irregular bright spots against a dark field that could drive surface detail later.

[add original-multifractal]
Distorted Voronoi defining droplet regions

On top of that I layered a Voronoi texture, distorted with a Mapping node and Vector Math to break up the regular cell pattern. The result is soft, blob-like regions across the surface — the shapes that would become individual water droplets.

[add normal-bump]
First normal map pass

Feeding the combined noise into a Normal Map node gave the first bump pass. The droplets read as small raised spots on the surface, but the scale was too fine and the shapes too uniform.

[add better-bump]
Tuned Musgrave — larger droplet bumps

Adjusting the Musgrave scale and dimension settings pushed the bumps larger and more teardrop-shaped, as if water is pooling and running down the surface.

[add metal-droplets]
Final render — metallic BSDF with droplet normals

The finished shader plugs the normal map into a metallic BSDF with a dark base color and high roughness variation. Specular highlights on each droplet sit against the brushed metal underneath.
