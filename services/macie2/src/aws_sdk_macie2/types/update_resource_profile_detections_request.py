"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateResourceProfileDetectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_suppress_data_identifier
    import aws_sdk_macie2.types.__string


class UpdateResourceProfileDetectionsRequest(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket that the request applies to.</p>"""
    suppress_data_identifiers: NotRequired[
        "aws_sdk_macie2.types.__list_of_suppress_data_identifier.__listOfSuppressDataIdentifier"
    ]
    """<p>An array of objects, one for each custom data identifier or managed data identifier that detected a type of sensitive data to exclude from the bucket's score. To include all sensitive data types in the score, don't specify any values for this array.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceProfileDetectionsRequest) -> dict:
    out: dict = {}
    if "suppress_data_identifiers" in value:
        import aws_sdk_macie2.types.__list_of_suppress_data_identifier

        out["suppressDataIdentifiers"] = (
            aws_sdk_macie2.types.__list_of_suppress_data_identifier.serialize_json(
                value["suppress_data_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateResourceProfileDetectionsRequest:
    out: UpdateResourceProfileDetectionsRequest = {}  # type: ignore[typeddict-item]
    if "suppressDataIdentifiers" in data:
        import aws_sdk_macie2.types.__list_of_suppress_data_identifier

        out["suppress_data_identifiers"] = (
            aws_sdk_macie2.types.__list_of_suppress_data_identifier.deserialize_json(
                data["suppressDataIdentifiers"]
            )
        )
    return out
