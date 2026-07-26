"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PatternToken``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.boolean
    import capo_cloudwatch_logs.types.dynamic_token_position
    import capo_cloudwatch_logs.types.enumerations
    import capo_cloudwatch_logs.types.inferred_token_name
    import capo_cloudwatch_logs.types.token_string


class PatternToken(TypedDict, closed=True):
    dynamic_token_position: (
        "capo_cloudwatch_logs.types.dynamic_token_position.DynamicTokenPosition"
    )
    """<p>For a dynamic token, this indicates where in the pattern that this token appears, related to other dynamic tokens. The dynamic token that appears first has a value of <code>1</code>, the one that appears second is <code>2</code>, and so on.</p>"""
    is_dynamic: NotRequired["capo_cloudwatch_logs.types.boolean.Boolean"]
    """<p>Specifies whether this is a dynamic token.</p>"""
    token_string: NotRequired["capo_cloudwatch_logs.types.token_string.TokenString"]
    """<p>The string represented by this token. If this is a dynamic token, the value will be <code><*></code> </p>"""
    enumerations: NotRequired["capo_cloudwatch_logs.types.enumerations.Enumerations"]
    """<p>Contains the values found for a dynamic token, and the number of times each value was found.</p>"""
    inferred_token_name: NotRequired[
        "capo_cloudwatch_logs.types.inferred_token_name.InferredTokenName"
    ]
    """<p>A name that CloudWatch Logs assigned to this dynamic token to make the pattern more readable. The string part of the <code>inferredTokenName</code> gives you a clearer idea of the content of this token. The number part of the <code>inferredTokenName</code> shows where in the pattern this token appears, compared to other dynamic tokens. CloudWatch Logs assigns the string part of the name based on analyzing the content of the log events that contain it.</p> <p>For example, an inferred token name of <code>IPAddress-3</code> means that the token represents an IP address, and this token is the third dynamic token in the pattern.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatternToken) -> dict:
    out: dict = {}
    out["dynamicTokenPosition"] = value.get("dynamic_token_position", 0)
    if "is_dynamic" in value:
        out["isDynamic"] = value["is_dynamic"]
    if "token_string" in value:
        out["tokenString"] = value["token_string"]
    if "enumerations" in value:
        import capo_cloudwatch_logs.types.enumerations

        out["enumerations"] = (
            capo_cloudwatch_logs.types.enumerations.serialize_aws_json_1_1(
                value["enumerations"]
            )
        )
    if "inferred_token_name" in value:
        out["inferredTokenName"] = value["inferred_token_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PatternToken:
    out: PatternToken = {}  # type: ignore[typeddict-item]
    if "dynamicTokenPosition" in data:
        out["dynamic_token_position"] = data["dynamicTokenPosition"]
    else:
        out["dynamic_token_position"] = 0
    if "isDynamic" in data:
        out["is_dynamic"] = data["isDynamic"]
    if "tokenString" in data:
        out["token_string"] = data["tokenString"]
    if "enumerations" in data:
        import capo_cloudwatch_logs.types.enumerations

        out["enumerations"] = (
            capo_cloudwatch_logs.types.enumerations.deserialize_aws_json_1_1(
                data["enumerations"]
            )
        )
    if "inferredTokenName" in data:
        out["inferred_token_name"] = data["inferredTokenName"]
    return out
