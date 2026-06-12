"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#JwtValidationActionAdditionalClaims``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim

JwtValidationActionAdditionalClaims: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim.JwtValidationActionAdditionalClaim"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: JwtValidationActionAdditionalClaims,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> JwtValidationActionAdditionalClaims:
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim

    out: JwtValidationActionAdditionalClaims = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: JwtValidationActionAdditionalClaims,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> JwtValidationActionAdditionalClaims:
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim

    out: JwtValidationActionAdditionalClaims = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim.deserialize_query(
                child
            )
        )
    return out
