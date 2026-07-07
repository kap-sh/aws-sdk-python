"""Generated from Smithy shape ``com.amazonaws.sns#CheckIfPhoneNumberIsOptedOutResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.boolean


class CheckIfPhoneNumberIsOptedOutResponse(TypedDict, closed=True):
    is_opted_out: "aws_sdk_sns.types.boolean.boolean"
    """<p>Indicates whether the phone number is opted out:</p> <ul> <li> <p> <code>true</code> – The phone number is opted out, meaning you cannot publish SMS messages to it.</p> </li> <li> <p> <code>false</code> – The phone number is opted in, meaning you can publish SMS messages to it.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CheckIfPhoneNumberIsOptedOutResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append(
        (
            f"{prefix}.isOptedOut",
            "true" if value.get("is_opted_out", False) else "false",
        )
    )


def deserialize_query(el: Element) -> CheckIfPhoneNumberIsOptedOutResponse:
    out: CheckIfPhoneNumberIsOptedOutResponse = {}  # type: ignore[typeddict-item]
    child_is_opted_out = el.find("isOptedOut")
    if child_is_opted_out is not None:
        out["is_opted_out"] = (child_is_opted_out.text or "").lower() == "true"
    else:
        out["is_opted_out"] = False
    return out
