"""Generated from Smithy shape ``com.amazonaws.redshift#CreateAuthenticationProfileResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.authentication_profile_name_string
    import aws_sdk_redshift.types.string


class CreateAuthenticationProfileResult(TypedDict):
    authentication_profile_name: NotRequired[
        "aws_sdk_redshift.types.authentication_profile_name_string.AuthenticationProfileNameString"
    ]
    """<p>The name of the authentication profile that was created.</p>"""
    authentication_profile_content: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The content of the authentication profile in JSON format.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateAuthenticationProfileResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "authentication_profile_name" in value:
        pairs.append(
            (
                f"{prefix}.AuthenticationProfileName",
                str(value["authentication_profile_name"]),
            )
        )
    if "authentication_profile_content" in value:
        pairs.append(
            (
                f"{prefix}.AuthenticationProfileContent",
                str(value["authentication_profile_content"]),
            )
        )


def deserialize_query(el: Element) -> CreateAuthenticationProfileResult:
    out: CreateAuthenticationProfileResult = {}  # type: ignore[typeddict-item]
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
