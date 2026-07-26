"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetComponentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.component
    import capo_ssm_sap.types.tag_map


class GetComponentOutput(TypedDict, closed=True):
    component: NotRequired["capo_ssm_sap.types.component.Component"]
    """<p>The component of an application registered with AWS Systems Manager for SAP.</p>"""
    tags: NotRequired["capo_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags of a component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentOutput) -> dict:
    out: dict = {}
    if "component" in value:
        import capo_ssm_sap.types.component

        out["Component"] = capo_ssm_sap.types.component.serialize_json(
            value["component"]
        )
    if "tags" in value:
        import capo_ssm_sap.types.tag_map

        out["Tags"] = capo_ssm_sap.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetComponentOutput:
    out: GetComponentOutput = {}  # type: ignore[typeddict-item]
    if "Component" in data:
        import capo_ssm_sap.types.component

        out["component"] = capo_ssm_sap.types.component.deserialize_json(
            data["Component"]
        )
    if "Tags" in data:
        import capo_ssm_sap.types.tag_map

        out["tags"] = capo_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    return out
