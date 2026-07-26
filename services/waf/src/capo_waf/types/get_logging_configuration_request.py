"""Generated from Smithy shape ``com.amazonaws.waf#GetLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.resource_arn


class GetLoggingConfigurationRequest(TypedDict, closed=True):
    resource_arn: "capo_waf.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL for which you want to get the <a>LoggingConfiguration</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLoggingConfigurationRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLoggingConfigurationRequest:
    out: GetLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "GetLoggingConfigurationRequest.resource_arn required"
        )
    return out
