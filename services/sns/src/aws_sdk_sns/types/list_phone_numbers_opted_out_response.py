"""Generated from Smithy shape ``com.amazonaws.sns#ListPhoneNumbersOptedOutResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.phone_number_list
    import aws_sdk_sns.types.string


class ListPhoneNumbersOptedOutResponse(TypedDict):
    phone_numbers: NotRequired["aws_sdk_sns.types.phone_number_list.PhoneNumberList"]
    """<p>A list of phone numbers that are opted out of receiving SMS messages. The list is paginated, and each page can contain up to 100 phone numbers.</p>"""
    next_token: NotRequired["aws_sdk_sns.types.string.String"]
    """<p>A <code>NextToken</code> string is returned when you call the <code>ListPhoneNumbersOptedOut</code> action if additional records are available after the first page of results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPhoneNumbersOptedOutResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "phone_numbers" in value:
        import aws_sdk_sns.types.phone_number_list

        aws_sdk_sns.types.phone_number_list.serialize_query(
            value["phone_numbers"], pairs, f"{prefix}.phoneNumbers"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.nextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListPhoneNumbersOptedOutResponse:
    out: ListPhoneNumbersOptedOutResponse = {}  # type: ignore[typeddict-item]
    child_phone_numbers = el.find("phoneNumbers")
    if child_phone_numbers is not None:
        import aws_sdk_sns.types.phone_number_list

        out["phone_numbers"] = aws_sdk_sns.types.phone_number_list.deserialize_query(
            child_phone_numbers
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
