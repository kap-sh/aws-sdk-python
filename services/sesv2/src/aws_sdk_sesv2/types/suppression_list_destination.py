"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionListDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.suppression_list_import_action


class SuppressionListDestination(TypedDict):
    suppression_list_import_action: (
        "aws_sdk_sesv2.types.suppression_list_import_action.SuppressionListImportAction"
    )
    """<p>The type of action to perform on the address. The following are possible values:</p> <ul> <li> <p>PUT: add the addresses to the suppression list. If the record already exists, it will override it with the new value.</p> </li> <li> <p>DELETE: remove the addresses from the suppression list.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionListDestination) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.suppression_list_import_action

    out["SuppressionListImportAction"] = (
        aws_sdk_sesv2.types.suppression_list_import_action.serialize_json(
            value["suppression_list_import_action"]
        )
    )
    return out


def deserialize_json(data: dict) -> SuppressionListDestination:
    out: SuppressionListDestination = {}  # type: ignore[typeddict-item]
    if "SuppressionListImportAction" in data:
        import aws_sdk_sesv2.types.suppression_list_import_action

        out["suppression_list_import_action"] = (
            aws_sdk_sesv2.types.suppression_list_import_action.deserialize_json(
                data["SuppressionListImportAction"]
            )
        )
    else:
        raise DeserializationError(
            "SuppressionListDestination.suppression_list_import_action required"
        )
    return out
