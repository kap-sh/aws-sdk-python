"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeCopyProductStatusInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id


class DescribeCopyProductStatusInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    copy_product_token: "aws_sdk_service_catalog.types.id.Id"
    """<p>The token for the copy product operation. This token is returned by <a>CopyProduct</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCopyProductStatusInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["CopyProductToken"] = value["copy_product_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCopyProductStatusInput:
    out: DescribeCopyProductStatusInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "CopyProductToken" in data:
        out["copy_product_token"] = data["CopyProductToken"]
    else:
        raise DeserializationError(
            "DescribeCopyProductStatusInput.copy_product_token required"
        )
    return out
