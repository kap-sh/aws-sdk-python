"""Generated from Smithy shape ``com.amazonaws.iam#CreateLoginProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.login_profile


class CreateLoginProfileResponse(TypedDict, closed=True):
    login_profile: "capo_iam.types.login_profile.LoginProfile"
    """<p>A structure containing the user name and password create date.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoginProfileResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.login_profile

    capo_iam.types.login_profile.serialize_query(
        value["login_profile"], pairs, f"{prefix}.LoginProfile"
    )


def deserialize_query(el: Element) -> CreateLoginProfileResponse:
    out: CreateLoginProfileResponse = {}  # type: ignore[typeddict-item]
    child_login_profile = el.find("LoginProfile")
    if child_login_profile is not None:
        import capo_iam.types.login_profile

        out["login_profile"] = capo_iam.types.login_profile.deserialize_query(
            child_login_profile
        )
    else:
        raise DeserializationError("CreateLoginProfileResponse.login_profile required")
    return out
