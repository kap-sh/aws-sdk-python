"""Generated from Smithy shape ``com.amazonaws.redshift#AuthenticationProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.authentication_profile_name_string
    import capo_redshift.types.string


class AuthenticationProfile(TypedDict, closed=True):
    authentication_profile_name: NotRequired[
        "capo_redshift.types.authentication_profile_name_string.AuthenticationProfileNameString"
    ]
    """<p>The name of the authentication profile.</p>"""
    authentication_profile_content: NotRequired["capo_redshift.types.string.String"]
    """<p>The content of the authentication profile in JSON format. The maximum length of the JSON string is determined by a quota for your account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthenticationProfile, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "authentication_profile_name" in value:
        pairs.append(
            (
                f"{key_prefix}AuthenticationProfileName",
                str(value["authentication_profile_name"]),
            )
        )
    if "authentication_profile_content" in value:
        pairs.append(
            (
                f"{key_prefix}AuthenticationProfileContent",
                str(value["authentication_profile_content"]),
            )
        )


def deserialize_query(el: Element) -> AuthenticationProfile:
    out: AuthenticationProfile = {}  # type: ignore[typeddict-item]
    child_authentication_profile_name = el.find("AuthenticationProfileName")
    if child_authentication_profile_name is not None:
        out["authentication_profile_name"] = str(
            child_authentication_profile_name.text or ""
        )
    child_authentication_profile_content = el.find("AuthenticationProfileContent")
    if child_authentication_profile_content is not None:
        out["authentication_profile_content"] = str(
            child_authentication_profile_content.text or ""
        )
    return out
