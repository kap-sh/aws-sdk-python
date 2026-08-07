"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeAuthenticationProfilesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.authentication_profile_name_string


class DescribeAuthenticationProfilesMessage(TypedDict, closed=True):
    authentication_profile_name: NotRequired[
        "capo_redshift.types.authentication_profile_name_string.AuthenticationProfileNameString"
    ]
    """<p>The name of the authentication profile to describe. If not specified then all authentication profiles owned by the account are listed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAuthenticationProfilesMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "authentication_profile_name" in value:
        pairs.append(
            (
                f"{key_prefix}AuthenticationProfileName",
                str(value["authentication_profile_name"]),
            )
        )


def deserialize_query(el: Element) -> DescribeAuthenticationProfilesMessage:
    out: DescribeAuthenticationProfilesMessage = {}  # type: ignore[typeddict-item]
    child_authentication_profile_name = el.find("AuthenticationProfileName")
    if child_authentication_profile_name is not None:
        out["authentication_profile_name"] = str(
            child_authentication_profile_name.text or ""
        )
    return out
