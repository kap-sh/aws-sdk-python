"""Generated from Smithy shape ``com.amazonaws.appintegrations#ContactHandling``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.contact_handling_scope


class ContactHandling(TypedDict, closed=True):
    scope: NotRequired[
        "aws_sdk_appintegrations.types.contact_handling_scope.ContactHandlingScope"
    ]
    """<p>Indicates whether the application refreshes for each contact or refreshes only with each new browser session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactHandling) -> dict:
    out: dict = {}
    if "scope" in value:
        import aws_sdk_appintegrations.types.contact_handling_scope

        out["Scope"] = (
            aws_sdk_appintegrations.types.contact_handling_scope.serialize_json(
                value["scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactHandling:
    out: ContactHandling = {}  # type: ignore[typeddict-item]
    if "Scope" in data:
        import aws_sdk_appintegrations.types.contact_handling_scope

        out["scope"] = (
            aws_sdk_appintegrations.types.contact_handling_scope.deserialize_json(
                data["Scope"]
            )
        )
    return out
