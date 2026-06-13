"""Generated from Smithy shape ``com.amazonaws.mailmanager#ReplaceRecipientAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.recipients


class ReplaceRecipientAction(TypedDict):
    replace_with: NotRequired["aws_sdk_mailmanager.types.recipients.Recipients"]
    """<p>This action specifies the replacement recipient email addresses to insert.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplaceRecipientAction) -> dict:
    out: dict = {}
    if "replace_with" in value:
        import aws_sdk_mailmanager.types.recipients

        out["ReplaceWith"] = (
            aws_sdk_mailmanager.types.recipients.serialize_aws_json_1_0(
                value["replace_with"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplaceRecipientAction:
    out: ReplaceRecipientAction = {}  # type: ignore[typeddict-item]
    if "ReplaceWith" in data:
        import aws_sdk_mailmanager.types.recipients

        out["replace_with"] = (
            aws_sdk_mailmanager.types.recipients.deserialize_aws_json_1_0(
                data["ReplaceWith"]
            )
        )
    return out
