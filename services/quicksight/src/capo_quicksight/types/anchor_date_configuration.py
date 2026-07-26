"""Generated from Smithy shape ``com.amazonaws.quicksight#AnchorDateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.anchor_option
    import capo_quicksight.types.parameter_name


class AnchorDateConfiguration(TypedDict, closed=True):
    anchor_option: NotRequired["capo_quicksight.types.anchor_option.AnchorOption"]
    """<p>The options for the date configuration. Choose one of the options below:</p> <ul> <li> <p> <code>NOW</code> </p> </li> </ul>"""
    parameter_name: NotRequired["capo_quicksight.types.parameter_name.ParameterName"]
    """<p>The name of the parameter that is used for the anchor date configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnchorDateConfiguration) -> dict:
    out: dict = {}
    if "anchor_option" in value:
        import capo_quicksight.types.anchor_option

        out["AnchorOption"] = capo_quicksight.types.anchor_option.serialize_json(
            value["anchor_option"]
        )
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    return out


def deserialize_json(data: dict) -> AnchorDateConfiguration:
    out: AnchorDateConfiguration = {}  # type: ignore[typeddict-item]
    if "AnchorOption" in data:
        import capo_quicksight.types.anchor_option

        out["anchor_option"] = capo_quicksight.types.anchor_option.deserialize_json(
            data["AnchorOption"]
        )
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    return out
