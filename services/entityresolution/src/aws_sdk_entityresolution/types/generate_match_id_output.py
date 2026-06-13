"""Generated from Smithy shape ``com.amazonaws.entityresolution#GenerateMatchIdOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.failed_records_list
    import aws_sdk_entityresolution.types.match_groups_list


class GenerateMatchIdOutput(TypedDict):
    match_groups: "aws_sdk_entityresolution.types.match_groups_list.MatchGroupsList"
    """<p> The match groups from the generated match ID.</p>"""
    failed_records: (
        "aws_sdk_entityresolution.types.failed_records_list.FailedRecordsList"
    )
    """<p> The records that didn't receive a generated Match ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateMatchIdOutput) -> dict:
    out: dict = {}
    import aws_sdk_entityresolution.types.match_groups_list

    out["matchGroups"] = (
        aws_sdk_entityresolution.types.match_groups_list.serialize_json(
            value["match_groups"]
        )
    )
    import aws_sdk_entityresolution.types.failed_records_list

    out["failedRecords"] = (
        aws_sdk_entityresolution.types.failed_records_list.serialize_json(
            value["failed_records"]
        )
    )
    return out


def deserialize_json(data: dict) -> GenerateMatchIdOutput:
    out: GenerateMatchIdOutput = {}  # type: ignore[typeddict-item]
    if "matchGroups" in data:
        import aws_sdk_entityresolution.types.match_groups_list

        out["match_groups"] = (
            aws_sdk_entityresolution.types.match_groups_list.deserialize_json(
                data["matchGroups"]
            )
        )
    else:
        raise DeserializationError("GenerateMatchIdOutput.match_groups required")
    if "failedRecords" in data:
        import aws_sdk_entityresolution.types.failed_records_list

        out["failed_records"] = (
            aws_sdk_entityresolution.types.failed_records_list.deserialize_json(
                data["failedRecords"]
            )
        )
    else:
        raise DeserializationError("GenerateMatchIdOutput.failed_records required")
    return out
