"""Generated from Smithy shape ``com.amazonaws.rds#RecommendedActionParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.recommended_action_parameter

RecommendedActionParameterList: TypeAlias = list[
    "aws_sdk_rds.types.recommended_action_parameter.RecommendedActionParameter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendedActionParameterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.recommended_action_parameter

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.recommended_action_parameter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RecommendedActionParameterList:
    import aws_sdk_rds.types.recommended_action_parameter

    out: RecommendedActionParameterList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_rds.types.recommended_action_parameter.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: RecommendedActionParameterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.recommended_action_parameter

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.recommended_action_parameter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RecommendedActionParameterList:
    import aws_sdk_rds.types.recommended_action_parameter

    out: RecommendedActionParameterList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_rds.types.recommended_action_parameter.deserialize_query(child)
        )
    return out
