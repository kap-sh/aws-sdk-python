"""Generated from Smithy shape ``com.amazonaws.athena#CreateCapacityReservationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.capacity_reservation_name
    import aws_sdk_athena.types.tag_list
    import aws_sdk_athena.types.target_dpus_integer


class CreateCapacityReservationInput(TypedDict, closed=True):
    target_dpus: "aws_sdk_athena.types.target_dpus_integer.TargetDpusInteger"
    """<p>The number of requested data processing units.</p>"""
    name: "aws_sdk_athena.types.capacity_reservation_name.CapacityReservationName"
    """<p>The name of the capacity reservation to create.</p>"""
    tags: NotRequired["aws_sdk_athena.types.tag_list.TagList"]
    """<p>The tags for the capacity reservation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCapacityReservationInput) -> dict:
    out: dict = {}
    out["TargetDpus"] = value["target_dpus"]
    out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_athena.types.tag_list

        out["Tags"] = aws_sdk_athena.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCapacityReservationInput:
    out: CreateCapacityReservationInput = {}  # type: ignore[typeddict-item]
    if "TargetDpus" in data:
        out["target_dpus"] = data["TargetDpus"]
    else:
        raise DeserializationError(
            "CreateCapacityReservationInput.target_dpus required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCapacityReservationInput.name required")
    if "Tags" in data:
        import aws_sdk_athena.types.tag_list

        out["tags"] = aws_sdk_athena.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
