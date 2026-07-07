"""Generated from Smithy shape ``com.amazonaws.ecr#GetAuthorizationTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.authorization_data_list


class GetAuthorizationTokenResponse(TypedDict, closed=True):
    authorization_data: NotRequired[
        "aws_sdk_ecr.types.authorization_data_list.AuthorizationDataList"
    ]
    """<p>A list of authorization token data objects that correspond to the <code>registryIds</code> values in the request.</p> <note> <p>The size of the authorization token returned by Amazon ECR is not fixed. We recommend that you don't make assumptions about the maximum size.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAuthorizationTokenResponse) -> dict:
    out: dict = {}
    if "authorization_data" in value:
        import aws_sdk_ecr.types.authorization_data_list

        out["authorizationData"] = (
            aws_sdk_ecr.types.authorization_data_list.serialize_aws_json_1_1(
                value["authorization_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAuthorizationTokenResponse:
    out: GetAuthorizationTokenResponse = {}  # type: ignore[typeddict-item]
    if "authorizationData" in data:
        import aws_sdk_ecr.types.authorization_data_list

        out["authorization_data"] = (
            aws_sdk_ecr.types.authorization_data_list.deserialize_aws_json_1_1(
                data["authorizationData"]
            )
        )
    return out
