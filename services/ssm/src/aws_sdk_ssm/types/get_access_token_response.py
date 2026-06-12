"""Generated from Smithy shape ``com.amazonaws.ssm#GetAccessTokenResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.access_request_status
    import aws_sdk_ssm.types.credentials


class GetAccessTokenResponse(TypedDict):
    credentials: NotRequired["aws_sdk_ssm.types.credentials.Credentials"]
    """<p>The temporary security credentials which can be used to start just-in-time node access sessions.</p>"""
    access_request_status: NotRequired[
        "aws_sdk_ssm.types.access_request_status.AccessRequestStatus"
    ]
    """<p>The status of the access request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccessTokenResponse) -> dict:
    out: dict = {}
    if "credentials" in value:
        import aws_sdk_ssm.types.credentials

        out["Credentials"] = aws_sdk_ssm.types.credentials.serialize_aws_json_1_1(
            value["credentials"]
        )
    if "access_request_status" in value:
        import aws_sdk_ssm.types.access_request_status

        out["AccessRequestStatus"] = (
            aws_sdk_ssm.types.access_request_status.serialize_aws_json_1_1(
                value["access_request_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccessTokenResponse:
    out: GetAccessTokenResponse = {}  # type: ignore[typeddict-item]
    if "Credentials" in data:
        import aws_sdk_ssm.types.credentials

        out["credentials"] = aws_sdk_ssm.types.credentials.deserialize_aws_json_1_1(
            data["Credentials"]
        )
    if "AccessRequestStatus" in data:
        import aws_sdk_ssm.types.access_request_status

        out["access_request_status"] = (
            aws_sdk_ssm.types.access_request_status.deserialize_aws_json_1_1(
                data["AccessRequestStatus"]
            )
        )
    return out
