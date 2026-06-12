"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EnableFederationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_store_arn
    import aws_sdk_cloudtrail.types.federation_role_arn
    import aws_sdk_cloudtrail.types.federation_status


class EnableFederationResponse(TypedDict):
    event_data_store_arn: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p> The ARN of the event data store for which you enabled Lake query federation. </p>"""
    federation_status: NotRequired[
        "aws_sdk_cloudtrail.types.federation_status.FederationStatus"
    ]
    """<p> The federation status. </p>"""
    federation_role_arn: NotRequired[
        "aws_sdk_cloudtrail.types.federation_role_arn.FederationRoleArn"
    ]
    """<p> The ARN of the federation role. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableFederationResponse) -> dict:
    out: dict = {}
    if "event_data_store_arn" in value:
        out["EventDataStoreArn"] = value["event_data_store_arn"]
    if "federation_status" in value:
        import aws_sdk_cloudtrail.types.federation_status

        out["FederationStatus"] = (
            aws_sdk_cloudtrail.types.federation_status.serialize_aws_json_1_1(
                value["federation_status"]
            )
        )
    if "federation_role_arn" in value:
        out["FederationRoleArn"] = value["federation_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableFederationResponse:
    out: EnableFederationResponse = {}  # type: ignore[typeddict-item]
    if "EventDataStoreArn" in data:
        out["event_data_store_arn"] = data["EventDataStoreArn"]
    if "FederationStatus" in data:
        import aws_sdk_cloudtrail.types.federation_status

        out["federation_status"] = (
            aws_sdk_cloudtrail.types.federation_status.deserialize_aws_json_1_1(
                data["FederationStatus"]
            )
        )
    if "FederationRoleArn" in data:
        out["federation_role_arn"] = data["FederationRoleArn"]
    return out
