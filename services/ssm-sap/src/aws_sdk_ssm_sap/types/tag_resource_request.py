"""Generated from Smithy shape ``com.amazonaws.ssmsap#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.ssm_sap_arn
    import aws_sdk_ssm_sap.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "aws_sdk_ssm_sap.types.tag_map.TagMap"
    """<p>The tags on a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_ssm_sap.types.tag_map

    out["tags"] = aws_sdk_ssm_sap.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_ssm_sap.types.tag_map

        out["tags"] = aws_sdk_ssm_sap.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
