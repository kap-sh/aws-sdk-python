"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConditionalSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean
    import aws_sdk_lex_models_v2.types.conditional_branches
    import aws_sdk_lex_models_v2.types.default_conditional_branch


class ConditionalSpecification(TypedDict):
    active: "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Determines whether a conditional branch is active. When <code>active</code> is false, the conditions are not evaluated.</p>"""
    conditional_branches: (
        "aws_sdk_lex_models_v2.types.conditional_branches.ConditionalBranches"
    )
    """<p>A list of conditional branches. A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.</p>"""
    default_branch: "aws_sdk_lex_models_v2.types.default_conditional_branch.DefaultConditionalBranch"
    """<p>The conditional branch that should be followed when the conditions for other branches are not satisfied. A conditional branch is made up of a condition, a response and a next step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalSpecification) -> dict:
    out: dict = {}
    out["active"] = value["active"]
    import aws_sdk_lex_models_v2.types.conditional_branches

    out["conditionalBranches"] = (
        aws_sdk_lex_models_v2.types.conditional_branches.serialize_json(
            value["conditional_branches"]
        )
    )
    import aws_sdk_lex_models_v2.types.default_conditional_branch

    out["defaultBranch"] = (
        aws_sdk_lex_models_v2.types.default_conditional_branch.serialize_json(
            value["default_branch"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConditionalSpecification:
    out: ConditionalSpecification = {}  # type: ignore[typeddict-item]
    if "active" in data:
        out["active"] = data["active"]
    else:
        raise DeserializationError("ConditionalSpecification.active required")
    if "conditionalBranches" in data:
        import aws_sdk_lex_models_v2.types.conditional_branches

        out["conditional_branches"] = (
            aws_sdk_lex_models_v2.types.conditional_branches.deserialize_json(
                data["conditionalBranches"]
            )
        )
    else:
        raise DeserializationError(
            "ConditionalSpecification.conditional_branches required"
        )
    if "defaultBranch" in data:
        import aws_sdk_lex_models_v2.types.default_conditional_branch

        out["default_branch"] = (
            aws_sdk_lex_models_v2.types.default_conditional_branch.deserialize_json(
                data["defaultBranch"]
            )
        )
    else:
        raise DeserializationError("ConditionalSpecification.default_branch required")
    return out
