"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteAuthenticationProfileResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.authentication_profile_name_string


class DeleteAuthenticationProfileResult(TypedDict, closed=True):
    authentication_profile_name: NotRequired[
        "aws_sdk_redshift.types.authentication_profile_name_string.AuthenticationProfileNameString"
    ]
    """<p>The name of the authentication profile that was deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAuthenticationProfileResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "authentication_profile_name" in value:
        pairs.append(
            (
                f"{prefix}.AuthenticationProfileName",
                str(value["authentication_profile_name"]),
            )
        )


def deserialize_query(el: Element) -> DeleteAuthenticationProfileResult:
    out: DeleteAuthenticationProfileResult = {}  # type: ignore[typeddict-item]
    child_authentication_profile_name = el.find("AuthenticationProfileName")
    if child_authentication_profile_name is not None:
        out["authentication_profile_name"] = str(
            child_authentication_profile_name.text or ""
        )
    return out
