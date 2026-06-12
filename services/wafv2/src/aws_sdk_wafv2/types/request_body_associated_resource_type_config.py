"""Generated from Smithy shape ``com.amazonaws.wafv2#RequestBodyAssociatedResourceTypeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.size_inspection_limit


class RequestBodyAssociatedResourceTypeConfig(TypedDict):
    default_size_inspection_limit: (
        "aws_sdk_wafv2.types.size_inspection_limit.SizeInspectionLimit"
    )
    """<p>Specifies the maximum size of the web request body component that an associated CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resource should send to WAF for inspection. This applies to statements in the web ACL that inspect the body or JSON body. </p> <p>Default: <code>16 KB (16,384 bytes)</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestBodyAssociatedResourceTypeConfig) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.size_inspection_limit

    out["DefaultSizeInspectionLimit"] = (
        aws_sdk_wafv2.types.size_inspection_limit.serialize_aws_json_1_1(
            value["default_size_inspection_limit"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestBodyAssociatedResourceTypeConfig:
    out: RequestBodyAssociatedResourceTypeConfig = {}  # type: ignore[typeddict-item]
    if "DefaultSizeInspectionLimit" in data:
        import aws_sdk_wafv2.types.size_inspection_limit

        out["default_size_inspection_limit"] = (
            aws_sdk_wafv2.types.size_inspection_limit.deserialize_aws_json_1_1(
                data["DefaultSizeInspectionLimit"]
            )
        )
    else:
        raise DeserializationError(
            "RequestBodyAssociatedResourceTypeConfig.default_size_inspection_limit required"
        )
    return out
