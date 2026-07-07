"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeServiceActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id


class DescribeServiceActionInput(TypedDict, closed=True):
    id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The self-service action identifier.</p>"""
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceActionInput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceActionInput:
    out: DescribeServiceActionInput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DescribeServiceActionInput.id required")
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    return out
