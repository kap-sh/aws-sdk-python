"""Generated from Smithy shape ``com.amazonaws.macie2#CreateSampleFindingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_finding_type


class CreateSampleFindingsRequest(TypedDict):
    finding_types: NotRequired[
        "aws_sdk_macie2.types.__list_of_finding_type.__listOfFindingType"
    ]
    """<p>An array of finding types, one for each type of sample finding to create. To create a sample of every type of finding that Amazon Macie supports, don't include this array in your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSampleFindingsRequest) -> dict:
    out: dict = {}
    if "finding_types" in value:
        import aws_sdk_macie2.types.__list_of_finding_type

        out["findingTypes"] = (
            aws_sdk_macie2.types.__list_of_finding_type.serialize_json(
                value["finding_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSampleFindingsRequest:
    out: CreateSampleFindingsRequest = {}  # type: ignore[typeddict-item]
    if "findingTypes" in data:
        import aws_sdk_macie2.types.__list_of_finding_type

        out["finding_types"] = (
            aws_sdk_macie2.types.__list_of_finding_type.deserialize_json(
                data["findingTypes"]
            )
        )
    return out
