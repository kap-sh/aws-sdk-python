"""Generated from Smithy shape ``com.amazonaws.connect#Filters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_statuses
    import aws_sdk_connect.types.channels
    import aws_sdk_connect.types.queues
    import aws_sdk_connect.types.routing_expressions
    import aws_sdk_connect.types.routing_profiles
    import aws_sdk_connect.types.subtypes
    import aws_sdk_connect.types.validation_test_types


class Filters(TypedDict, closed=True):
    queues: NotRequired["aws_sdk_connect.types.queues.Queues"]
    """<p>The queues to use to filter the metrics. You should specify at least one queue, and can specify up to 100 queues per request. The <code>GetCurrentMetricsData</code> API in particular requires a queue when you include a <code>Filter</code> in your request. </p>"""
    channels: NotRequired["aws_sdk_connect.types.channels.Channels"]
    """<p>The channel to use to filter the metrics.</p>"""
    routing_profiles: NotRequired[
        "aws_sdk_connect.types.routing_profiles.RoutingProfiles"
    ]
    """<p>A list of up to 100 routing profile IDs or ARNs.</p>"""
    routing_step_expressions: NotRequired[
        "aws_sdk_connect.types.routing_expressions.RoutingExpressions"
    ]
    """<p>A list of expressions as a filter, in which an expression is an object of a step in a routing criteria.</p>"""
    agent_statuses: NotRequired["aws_sdk_connect.types.agent_statuses.AgentStatuses"]
    """<p>A list of up to 50 agent status IDs or ARNs.</p>"""
    subtypes: NotRequired["aws_sdk_connect.types.subtypes.Subtypes"]
    """<p>A list of up to 10 subtypes can be provided.</p>"""
    validation_test_types: NotRequired[
        "aws_sdk_connect.types.validation_test_types.ValidationTestTypes"
    ]
    """<p>A list of up to 10 validationTestTypes can be provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filters) -> dict:
    out: dict = {}
    if "queues" in value:
        import aws_sdk_connect.types.queues

        out["Queues"] = aws_sdk_connect.types.queues.serialize_json(value["queues"])
    if "channels" in value:
        import aws_sdk_connect.types.channels

        out["Channels"] = aws_sdk_connect.types.channels.serialize_json(
            value["channels"]
        )
    if "routing_profiles" in value:
        import aws_sdk_connect.types.routing_profiles

        out["RoutingProfiles"] = aws_sdk_connect.types.routing_profiles.serialize_json(
            value["routing_profiles"]
        )
    if "routing_step_expressions" in value:
        import aws_sdk_connect.types.routing_expressions

        out["RoutingStepExpressions"] = (
            aws_sdk_connect.types.routing_expressions.serialize_json(
                value["routing_step_expressions"]
            )
        )
    if "agent_statuses" in value:
        import aws_sdk_connect.types.agent_statuses

        out["AgentStatuses"] = aws_sdk_connect.types.agent_statuses.serialize_json(
            value["agent_statuses"]
        )
    if "subtypes" in value:
        import aws_sdk_connect.types.subtypes

        out["Subtypes"] = aws_sdk_connect.types.subtypes.serialize_json(
            value["subtypes"]
        )
    if "validation_test_types" in value:
        import aws_sdk_connect.types.validation_test_types

        out["ValidationTestTypes"] = (
            aws_sdk_connect.types.validation_test_types.serialize_json(
                value["validation_test_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> Filters:
    out: Filters = {}  # type: ignore[typeddict-item]
    if "Queues" in data:
        import aws_sdk_connect.types.queues

        out["queues"] = aws_sdk_connect.types.queues.deserialize_json(data["Queues"])
    if "Channels" in data:
        import aws_sdk_connect.types.channels

        out["channels"] = aws_sdk_connect.types.channels.deserialize_json(
            data["Channels"]
        )
    if "RoutingProfiles" in data:
        import aws_sdk_connect.types.routing_profiles

        out["routing_profiles"] = (
            aws_sdk_connect.types.routing_profiles.deserialize_json(
                data["RoutingProfiles"]
            )
        )
    if "RoutingStepExpressions" in data:
        import aws_sdk_connect.types.routing_expressions

        out["routing_step_expressions"] = (
            aws_sdk_connect.types.routing_expressions.deserialize_json(
                data["RoutingStepExpressions"]
            )
        )
    if "AgentStatuses" in data:
        import aws_sdk_connect.types.agent_statuses

        out["agent_statuses"] = aws_sdk_connect.types.agent_statuses.deserialize_json(
            data["AgentStatuses"]
        )
    if "Subtypes" in data:
        import aws_sdk_connect.types.subtypes

        out["subtypes"] = aws_sdk_connect.types.subtypes.deserialize_json(
            data["Subtypes"]
        )
    if "ValidationTestTypes" in data:
        import aws_sdk_connect.types.validation_test_types

        out["validation_test_types"] = (
            aws_sdk_connect.types.validation_test_types.deserialize_json(
                data["ValidationTestTypes"]
            )
        )
    return out
