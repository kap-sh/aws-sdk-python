"""Generated from Smithy shape ``com.amazonaws.shield#SubResourceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.string
    import aws_sdk_shield.types.sub_resource_type
    import aws_sdk_shield.types.summarized_attack_vector_list
    import aws_sdk_shield.types.summarized_counter_list


class SubResourceSummary(TypedDict):
    type: NotRequired["aws_sdk_shield.types.sub_resource_type.SubResourceType"]
    """<p>The <code>SubResource</code> type.</p>"""
    id: NotRequired["aws_sdk_shield.types.string.String"]
    """<p>The unique identifier (ID) of the <code>SubResource</code>.</p>"""
    attack_vectors: NotRequired[
        "aws_sdk_shield.types.summarized_attack_vector_list.SummarizedAttackVectorList"
    ]
    """<p>The list of attack types and associated counters.</p>"""
    counters: NotRequired[
        "aws_sdk_shield.types.summarized_counter_list.SummarizedCounterList"
    ]
    """<p>The counters that describe the details of the attack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubResourceSummary) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_shield.types.sub_resource_type

        out["Type"] = aws_sdk_shield.types.sub_resource_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "attack_vectors" in value:
        import aws_sdk_shield.types.summarized_attack_vector_list

        out["AttackVectors"] = (
            aws_sdk_shield.types.summarized_attack_vector_list.serialize_aws_json_1_1(
                value["attack_vectors"]
            )
        )
    if "counters" in value:
        import aws_sdk_shield.types.summarized_counter_list

        out["Counters"] = (
            aws_sdk_shield.types.summarized_counter_list.serialize_aws_json_1_1(
                value["counters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubResourceSummary:
    out: SubResourceSummary = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_shield.types.sub_resource_type

        out["type"] = aws_sdk_shield.types.sub_resource_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "AttackVectors" in data:
        import aws_sdk_shield.types.summarized_attack_vector_list

        out["attack_vectors"] = (
            aws_sdk_shield.types.summarized_attack_vector_list.deserialize_aws_json_1_1(
                data["AttackVectors"]
            )
        )
    if "Counters" in data:
        import aws_sdk_shield.types.summarized_counter_list

        out["counters"] = (
            aws_sdk_shield.types.summarized_counter_list.deserialize_aws_json_1_1(
                data["Counters"]
            )
        )
    return out
