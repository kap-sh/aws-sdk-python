"""Generated from Smithy shape ``com.amazonaws.iam#GetLoginProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.login_profile


class GetLoginProfileResponse(TypedDict):
    login_profile: "aws_sdk_iam.types.login_profile.LoginProfile"
    """<p>A structure containing the user name and the profile creation date for the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetLoginProfileResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.login_profile

    aws_sdk_iam.types.login_profile.serialize_query(
        value["login_profile"], pairs, f"{prefix}.LoginProfile"
    )


def deserialize_query(el: Element) -> GetLoginProfileResponse:
    out: GetLoginProfileResponse = {}  # type: ignore[typeddict-item]
    child_login_profile = el.find("LoginProfile")
    if child_login_profile is not None:
        import aws_sdk_iam.types.login_profile

        out["login_profile"] = aws_sdk_iam.types.login_profile.deserialize_query(
            child_login_profile
        )
    else:
        raise DeserializationError("GetLoginProfileResponse.login_profile required")
    return out
