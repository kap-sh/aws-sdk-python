"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetApplicationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.application
    import capo_ssm_sap.types.tag_map


class GetApplicationOutput(TypedDict, closed=True):
    application: NotRequired["capo_ssm_sap.types.application.Application"]
    """<p>Returns all of the metadata of an application registered with AWS Systems Manager for SAP.</p>"""
    tags: NotRequired["capo_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags of a registered application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationOutput) -> dict:
    out: dict = {}
    if "application" in value:
        import capo_ssm_sap.types.application

        out["Application"] = capo_ssm_sap.types.application.serialize_json(
            value["application"]
        )
    if "tags" in value:
        import capo_ssm_sap.types.tag_map

        out["Tags"] = capo_ssm_sap.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetApplicationOutput:
    out: GetApplicationOutput = {}  # type: ignore[typeddict-item]
    if "Application" in data:
        import capo_ssm_sap.types.application

        out["application"] = capo_ssm_sap.types.application.deserialize_json(
            data["Application"]
        )
    if "Tags" in data:
        import capo_ssm_sap.types.tag_map

        out["tags"] = capo_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    return out
