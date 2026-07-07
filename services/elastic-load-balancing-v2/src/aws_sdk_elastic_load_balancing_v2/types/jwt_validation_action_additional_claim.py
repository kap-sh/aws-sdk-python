"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#JwtValidationActionAdditionalClaim``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_format_enum
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_name
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_values


class JwtValidationActionAdditionalClaim(TypedDict, closed=True):
    format: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_format_enum.JwtValidationActionAdditionalClaimFormatEnum"
    ]
    """<p>The format of the claim value.</p>"""
    name: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_name.JwtValidationActionAdditionalClaimName"
    ]
    """<p>The name of the claim. You can't specify <code>exp</code>, <code>iss</code>, <code>nbf</code>, or <code>iat</code> because we validate them by default.</p>"""
    values: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_values.JwtValidationActionAdditionalClaimValues"
    ]
    """<p>The claim value. The maximum size of the list is 10. Each value can be up to 256 characters in length. If the format is <code>space-separated-values</code>, the values can't include spaces.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: JwtValidationActionAdditionalClaim, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "format" in value:
        import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_format_enum

        aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_format_enum.serialize_query(
            value["format"], pairs, f"{prefix}.Format"
        )
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "values" in value:
        import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_values

        aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_values.serialize_query(
            value["values"], pairs, f"{prefix}.Values"
        )


def deserialize_query(el: Element) -> JwtValidationActionAdditionalClaim:
    out: JwtValidationActionAdditionalClaim = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_format_enum

        out["format"] = (
            aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_format_enum.deserialize_query(
                child_format
            )
        )
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_values

        out["values"] = (
            aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claim_values.deserialize_query(
                child_values
            )
        )
    return out
