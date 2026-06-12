"""Generated from Smithy shape ``com.amazonaws.licensemanager#AcceptGrantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn


class AcceptGrantRequest(TypedDict):
    grant_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptGrantRequest) -> dict:
    out: dict = {}
    out["GrantArn"] = value["grant_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptGrantRequest:
    out: AcceptGrantRequest = {}  # type: ignore[typeddict-item]
    if "GrantArn" in data:
        out["grant_arn"] = data["GrantArn"]
    else:
        raise DeserializationError("AcceptGrantRequest.grant_arn required")
    return out
