"""Generated from Smithy shape ``com.amazonaws.ecrpublic#GetAuthorizationTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.authorization_data


class GetAuthorizationTokenResponse(TypedDict, closed=True):
    authorization_data: NotRequired[
        "capo_ecr_public.types.authorization_data.AuthorizationData"
    ]
    """<p>An authorization token data object that corresponds to a public registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAuthorizationTokenResponse) -> dict:
    out: dict = {}
    if "authorization_data" in value:
        import capo_ecr_public.types.authorization_data

        out["authorizationData"] = (
            capo_ecr_public.types.authorization_data.serialize_aws_json_1_1(
                value["authorization_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAuthorizationTokenResponse:
    out: GetAuthorizationTokenResponse = {}  # type: ignore[typeddict-item]
    if "authorizationData" in data:
        import capo_ecr_public.types.authorization_data

        out["authorization_data"] = (
            capo_ecr_public.types.authorization_data.deserialize_aws_json_1_1(
                data["authorizationData"]
            )
        )
    return out
