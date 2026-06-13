"""Generated from Smithy shape ``com.amazonaws.ssmsap#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.ssm_sap_arn
    import aws_sdk_ssm_sap.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "aws_sdk_ssm_sap.types.tag_key_list.TagKeyList"
    """<p>Adds/updates or removes credentials for applications registered with AWS Systems Manager for SAP.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
