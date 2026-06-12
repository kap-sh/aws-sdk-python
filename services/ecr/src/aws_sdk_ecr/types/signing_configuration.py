"""Generated from Smithy shape ``com.amazonaws.ecr#SigningConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.signing_rule_list


class SigningConfiguration(TypedDict):
    rules: "aws_sdk_ecr.types.signing_rule_list.SigningRuleList"
    """<p>A list of signing rules. Each rule defines a signing profile and optional repository filters that determine which images are automatically signed. Maximum of 10 rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_ecr.types.signing_rule_list

    out["rules"] = aws_sdk_ecr.types.signing_rule_list.serialize_aws_json_1_1(
        value["rules"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SigningConfiguration:
    out: SigningConfiguration = {}  # type: ignore[typeddict-item]
    if "rules" in data:
        import aws_sdk_ecr.types.signing_rule_list

        out["rules"] = aws_sdk_ecr.types.signing_rule_list.deserialize_aws_json_1_1(
            data["rules"]
        )
    else:
        raise DeserializationError("SigningConfiguration.rules required")
    return out
