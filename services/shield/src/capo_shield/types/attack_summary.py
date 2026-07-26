"""Generated from Smithy shape ``com.amazonaws.shield#AttackSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.attack_timestamp
    import capo_shield.types.attack_vector_description_list
    import capo_shield.types.string


class AttackSummary(TypedDict, closed=True):
    attack_id: NotRequired["capo_shield.types.string.String"]
    """<p>The unique identifier (ID) of the attack.</p>"""
    resource_arn: NotRequired["capo_shield.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the resource that was attacked.</p>"""
    start_time: NotRequired["capo_shield.types.attack_timestamp.AttackTimestamp"]
    """<p>The start time of the attack, in Unix time in seconds. </p>"""
    end_time: NotRequired["capo_shield.types.attack_timestamp.AttackTimestamp"]
    """<p>The end time of the attack, in Unix time in seconds. </p>"""
    attack_vectors: NotRequired[
        "capo_shield.types.attack_vector_description_list.AttackVectorDescriptionList"
    ]
    """<p>The list of attacks for a specified time period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackSummary) -> dict:
    out: dict = {}
    if "attack_id" in value:
        out["AttackId"] = value["attack_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "start_time" in value:
        import capo_shield.types.attack_timestamp

        out["StartTime"] = capo_shield.types.attack_timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_shield.types.attack_timestamp

        out["EndTime"] = capo_shield.types.attack_timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "attack_vectors" in value:
        import capo_shield.types.attack_vector_description_list

        out["AttackVectors"] = (
            capo_shield.types.attack_vector_description_list.serialize_aws_json_1_1(
                value["attack_vectors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackSummary:
    out: AttackSummary = {}  # type: ignore[typeddict-item]
    if "AttackId" in data:
        out["attack_id"] = data["AttackId"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "StartTime" in data:
        import capo_shield.types.attack_timestamp

        out["start_time"] = capo_shield.types.attack_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_shield.types.attack_timestamp

        out["end_time"] = capo_shield.types.attack_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "AttackVectors" in data:
        import capo_shield.types.attack_vector_description_list

        out["attack_vectors"] = (
            capo_shield.types.attack_vector_description_list.deserialize_aws_json_1_1(
                data["AttackVectors"]
            )
        )
    return out
