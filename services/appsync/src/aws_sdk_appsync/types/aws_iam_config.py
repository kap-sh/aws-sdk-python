"""Generated from Smithy shape ``com.amazonaws.appsync#AwsIamConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class AwsIamConfig(TypedDict):
    signing_region: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The signing Amazon Web Services Region for IAM authorization.</p>"""
    signing_service_name: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The signing service name for IAM authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamConfig) -> dict:
    out: dict = {}
    if "signing_region" in value:
        out["signingRegion"] = value["signing_region"]
    if "signing_service_name" in value:
        out["signingServiceName"] = value["signing_service_name"]
    return out


def deserialize_json(data: dict) -> AwsIamConfig:
    out: AwsIamConfig = {}  # type: ignore[typeddict-item]
    if "signingRegion" in data:
        out["signing_region"] = data["signingRegion"]
    if "signingServiceName" in data:
        out["signing_service_name"] = data["signingServiceName"]
    return out
