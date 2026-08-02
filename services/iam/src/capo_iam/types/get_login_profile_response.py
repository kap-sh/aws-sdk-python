"""Generated from Smithy shape ``com.amazonaws.iam#GetLoginProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.login_profile


class GetLoginProfileResponse(TypedDict, closed=True):
    login_profile: "capo_iam.types.login_profile.LoginProfile"
    """<p>A structure containing the user name and the profile creation date for the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetLoginProfileResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.login_profile

    capo_iam.types.login_profile.serialize_query(
        value["login_profile"], pairs, f"{key_prefix}LoginProfile"
    )


def deserialize_query(el: Element) -> GetLoginProfileResponse:
    out: GetLoginProfileResponse = {}  # type: ignore[typeddict-item]
    child_login_profile = el.find("LoginProfile")
    if child_login_profile is not None:
        import capo_iam.types.login_profile

        out["login_profile"] = capo_iam.types.login_profile.deserialize_query(
            child_login_profile
        )
    else:
        raise DeserializationError("GetLoginProfileResponse.login_profile required")
    return out
