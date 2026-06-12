"""Generated from Smithy shape ``com.amazonaws.amplifybackend#BackendStoragePermissions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.list_of_authenticated_element
    import aws_sdk_amplifybackend.types.list_of_un_authenticated_element


class BackendStoragePermissions(TypedDict):
    authenticated: NotRequired[
        "aws_sdk_amplifybackend.types.list_of_authenticated_element.ListOfAuthenticatedElement"
    ]
    """<p>Lists all authenticated user read, write, and delete permissions for your S3 bucket.</p>"""
    un_authenticated: NotRequired[
        "aws_sdk_amplifybackend.types.list_of_un_authenticated_element.ListOfUnAuthenticatedElement"
    ]
    """<p>Lists all unauthenticated user read, write, and delete permissions for your S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendStoragePermissions) -> dict:
    out: dict = {}
    if "authenticated" in value:
        import aws_sdk_amplifybackend.types.list_of_authenticated_element

        out["authenticated"] = (
            aws_sdk_amplifybackend.types.list_of_authenticated_element.serialize_json(
                value["authenticated"]
            )
        )
    if "un_authenticated" in value:
        import aws_sdk_amplifybackend.types.list_of_un_authenticated_element

        out["unAuthenticated"] = (
            aws_sdk_amplifybackend.types.list_of_un_authenticated_element.serialize_json(
                value["un_authenticated"]
            )
        )
    return out


def deserialize_json(data: dict) -> BackendStoragePermissions:
    out: BackendStoragePermissions = {}  # type: ignore[typeddict-item]
    if "authenticated" in data:
        import aws_sdk_amplifybackend.types.list_of_authenticated_element

        out["authenticated"] = (
            aws_sdk_amplifybackend.types.list_of_authenticated_element.deserialize_json(
                data["authenticated"]
            )
        )
    if "unAuthenticated" in data:
        import aws_sdk_amplifybackend.types.list_of_un_authenticated_element

        out["un_authenticated"] = (
            aws_sdk_amplifybackend.types.list_of_un_authenticated_element.deserialize_json(
                data["unAuthenticated"]
            )
        )
    return out
