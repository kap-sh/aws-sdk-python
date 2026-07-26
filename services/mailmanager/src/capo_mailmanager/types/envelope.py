"""Generated from Smithy shape ``com.amazonaws.mailmanager#Envelope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.string_list

Envelope = TypedDict(
    "Envelope",
    {
        "helo": NotRequired["str"],
        "from": NotRequired["str"],
        "to": NotRequired["capo_mailmanager.types.string_list.StringList"],
    },
    closed=True,
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Envelope) -> dict:
    out: dict = {}
    if "helo" in value:
        out["Helo"] = value["helo"]
    if "from" in value:
        out["From"] = value["from"]
    if "to" in value:
        import capo_mailmanager.types.string_list

        out["To"] = capo_mailmanager.types.string_list.serialize_aws_json_1_0(
            value["to"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Envelope:
    out: Envelope = {}  # type: ignore[typeddict-item]
    if "Helo" in data:
        out["helo"] = data["Helo"]
    if "From" in data:
        out["from"] = data["From"]
    if "To" in data:
        import capo_mailmanager.types.string_list

        out["to"] = capo_mailmanager.types.string_list.deserialize_aws_json_1_0(
            data["To"]
        )
    return out
