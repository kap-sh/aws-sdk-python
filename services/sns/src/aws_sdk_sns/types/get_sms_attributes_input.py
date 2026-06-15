"""Generated from Smithy shape ``com.amazonaws.sns#GetSMSAttributesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.list_string


class GetSMSAttributesInput(TypedDict):
    attributes: NotRequired["aws_sdk_sns.types.list_string.ListString"]
    r"""<p>A list of the individual attribute names, such as <code>MonthlySpendLimit</code>, for which you want values.</p> <p>For all attribute names, see <a href=\"https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html\">SetSMSAttributes</a>.</p> <p>If you don't use this parameter, Amazon SNS returns all SMS attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSMSAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attributes" in value:
        import aws_sdk_sns.types.list_string

        aws_sdk_sns.types.list_string.serialize_query(
            value["attributes"], pairs, f"{prefix}.attributes"
        )


def deserialize_query(el: Element) -> GetSMSAttributesInput:
    out: GetSMSAttributesInput = {}  # type: ignore[typeddict-item]
    child_attributes = el.find("attributes")
    if child_attributes is not None:
        import aws_sdk_sns.types.list_string

        out["attributes"] = aws_sdk_sns.types.list_string.deserialize_query(
            child_attributes
        )
    return out
