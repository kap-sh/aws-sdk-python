"""Generated from Smithy shape ``com.amazonaws.geomaps#GetSpritesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_maps.types.color_scheme
    import capo_geo_maps.types.map_style
    import capo_geo_maps.types.variant


class GetSpritesRequest(TypedDict, closed=True):
    file_name: "str"
    r"""<p> <code>Sprites</code> API: The name of the sprite ﬁle to retrieve, following pattern <code>sprites(@2x)?\.(png|json)</code>.</p> <p>Example: <code>sprites.png</code> </p>"""
    style: "capo_geo_maps.types.map_style.MapStyle"
    """<p>Style specifies the desired map style for the <code>Sprites</code> APIs.</p>"""
    color_scheme: "capo_geo_maps.types.color_scheme.ColorScheme"
    """<p>Sets the color tone for the map sprites, such as dark and light.</p> <p>Example: <code>Light</code> </p> <p>Default value: <code>Light</code> </p> <note> <p>Valid values for ColorScheme are case sensitive.</p> </note>"""
    variant: "capo_geo_maps.types.variant.Variant"
    """<p>Optimizes map styles for specific use case or industry. You can choose allowed variant only with Standard map style.</p> <p>Example: <code>Default</code> </p> <note> <p>Valid values for Variant are case sensitive.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpritesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSpritesRequest:
    out: GetSpritesRequest = {}  # type: ignore[typeddict-item]
    return out
