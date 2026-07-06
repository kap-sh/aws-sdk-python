"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateSecurityConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.security_config_detail


class UpdateSecurityConfigResponse(TypedDict, closed=True):
    security_config_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.security_config_detail.SecurityConfigDetail"
    ]
    """<p>Details about the updated security configuration. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSecurityConfigResponse) -> dict:
    out: dict = {}
    if "security_config_detail" in value:
        import aws_sdk_opensearchserverless.types.security_config_detail

        out["securityConfigDetail"] = (
            aws_sdk_opensearchserverless.types.security_config_detail.serialize_aws_json_1_0(
                value["security_config_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSecurityConfigResponse:
    out: UpdateSecurityConfigResponse = {}  # type: ignore[typeddict-item]
    if "securityConfigDetail" in data:
        import aws_sdk_opensearchserverless.types.security_config_detail

        out["security_config_detail"] = (
            aws_sdk_opensearchserverless.types.security_config_detail.deserialize_aws_json_1_0(
                data["securityConfigDetail"]
            )
        )
    return out
