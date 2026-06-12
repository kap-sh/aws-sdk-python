"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateRuleVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.language
    import aws_sdk_frauddetector.types.non_empty_list_of_strings
    import aws_sdk_frauddetector.types.rule
    import aws_sdk_frauddetector.types.rule_expression
    import aws_sdk_frauddetector.types.tag_list


class UpdateRuleVersionRequest(TypedDict):
    rule: "aws_sdk_frauddetector.types.rule.Rule"
    """<p>The rule to update.</p>"""
    description: NotRequired["aws_sdk_frauddetector.types.description.description"]
    """<p>The description.</p>"""
    expression: "aws_sdk_frauddetector.types.rule_expression.ruleExpression"
    """<p>The rule expression.</p>"""
    language: "aws_sdk_frauddetector.types.language.Language"
    """<p>The language.</p>"""
    outcomes: (
        "aws_sdk_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings"
    )
    """<p>The outcomes.</p>"""
    tags: NotRequired["aws_sdk_frauddetector.types.tag_list.tagList"]
    """<p>The tags to assign to the rule version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuleVersionRequest) -> dict:
    out: dict = {}
    import aws_sdk_frauddetector.types.rule

    out["rule"] = aws_sdk_frauddetector.types.rule.serialize_aws_json_1_1(value["rule"])
    if "description" in value:
        out["description"] = value["description"]
    out["expression"] = value["expression"]
    import aws_sdk_frauddetector.types.language

    out["language"] = aws_sdk_frauddetector.types.language.serialize_aws_json_1_1(
        value["language"]
    )
    import aws_sdk_frauddetector.types.non_empty_list_of_strings

    out["outcomes"] = (
        aws_sdk_frauddetector.types.non_empty_list_of_strings.serialize_aws_json_1_1(
            value["outcomes"]
        )
    )
    if "tags" in value:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuleVersionRequest:
    out: UpdateRuleVersionRequest = {}  # type: ignore[typeddict-item]
    if "rule" in data:
        import aws_sdk_frauddetector.types.rule

        out["rule"] = aws_sdk_frauddetector.types.rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    else:
        raise DeserializationError("UpdateRuleVersionRequest.rule required")
    if "description" in data:
        out["description"] = data["description"]
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("UpdateRuleVersionRequest.expression required")
    if "language" in data:
        import aws_sdk_frauddetector.types.language

        out["language"] = aws_sdk_frauddetector.types.language.deserialize_aws_json_1_1(
            data["language"]
        )
    else:
        raise DeserializationError("UpdateRuleVersionRequest.language required")
    if "outcomes" in data:
        import aws_sdk_frauddetector.types.non_empty_list_of_strings

        out["outcomes"] = (
            aws_sdk_frauddetector.types.non_empty_list_of_strings.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    else:
        raise DeserializationError("UpdateRuleVersionRequest.outcomes required")
    if "tags" in data:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
