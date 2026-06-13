"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetApplicationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application
    import aws_sdk_ssm_sap.types.tag_map


class GetApplicationOutput(TypedDict):
    application: NotRequired["aws_sdk_ssm_sap.types.application.Application"]
    """<p>Returns all of the metadata of an application registered with AWS Systems Manager for SAP.</p>"""
    tags: NotRequired["aws_sdk_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags of a registered application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationOutput) -> dict:
    out: dict = {}
    if "application" in value:
        import aws_sdk_ssm_sap.types.application

        out["Application"] = aws_sdk_ssm_sap.types.application.serialize_json(
            value["application"]
        )
    if "tags" in value:
        import aws_sdk_ssm_sap.types.tag_map

        out["Tags"] = aws_sdk_ssm_sap.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetApplicationOutput:
    out: GetApplicationOutput = {}  # type: ignore[typeddict-item]
    if "Application" in data:
        import aws_sdk_ssm_sap.types.application

        out["application"] = aws_sdk_ssm_sap.types.application.deserialize_json(
            data["Application"]
        )
    if "Tags" in data:
        import aws_sdk_ssm_sap.types.tag_map

        out["tags"] = aws_sdk_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    return out
