"""Generated from Smithy shape ``com.amazonaws.connect#Filters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_statuses
    import capo_connect.types.channels
    import capo_connect.types.queues
    import capo_connect.types.routing_expressions
    import capo_connect.types.routing_profiles
    import capo_connect.types.subtypes
    import capo_connect.types.validation_test_types


class Filters(TypedDict, closed=True):
    queues: NotRequired["capo_connect.types.queues.Queues"]
    """<p>The queues to use to filter the metrics. You should specify at least one queue, and can specify up to 100 queues per request. The <code>GetCurrentMetricsData</code> API in particular requires a queue when you include a <code>Filter</code> in your request. </p>"""
    channels: NotRequired["capo_connect.types.channels.Channels"]
    """<p>The channel to use to filter the metrics.</p>"""
    routing_profiles: NotRequired["capo_connect.types.routing_profiles.RoutingProfiles"]
    """<p>A list of up to 100 routing profile IDs or ARNs.</p>"""
    routing_step_expressions: NotRequired[
        "capo_connect.types.routing_expressions.RoutingExpressions"
    ]
    """<p>A list of expressions as a filter, in which an expression is an object of a step in a routing criteria.</p>"""
    agent_statuses: NotRequired["capo_connect.types.agent_statuses.AgentStatuses"]
    """<p>A list of up to 50 agent status IDs or ARNs.</p>"""
    subtypes: NotRequired["capo_connect.types.subtypes.Subtypes"]
    """<p>A list of up to 10 subtypes can be provided.</p>"""
    validation_test_types: NotRequired[
        "capo_connect.types.validation_test_types.ValidationTestTypes"
    ]
    """<p>A list of up to 10 validationTestTypes can be provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filters) -> dict:
    out: dict = {}
    if "queues" in value:
        import capo_connect.types.queues

        out["Queues"] = capo_connect.types.queues.serialize_json(value["queues"])
    if "channels" in value:
        import capo_connect.types.channels

        out["Channels"] = capo_connect.types.channels.serialize_json(value["channels"])
    if "routing_profiles" in value:
        import capo_connect.types.routing_profiles

        out["RoutingProfiles"] = capo_connect.types.routing_profiles.serialize_json(
            value["routing_profiles"]
        )
    if "routing_step_expressions" in value:
        import capo_connect.types.routing_expressions

        out["RoutingStepExpressions"] = (
            capo_connect.types.routing_expressions.serialize_json(
                value["routing_step_expressions"]
            )
        )
    if "agent_statuses" in value:
        import capo_connect.types.agent_statuses

        out["AgentStatuses"] = capo_connect.types.agent_statuses.serialize_json(
            value["agent_statuses"]
        )
    if "subtypes" in value:
        import capo_connect.types.subtypes

        out["Subtypes"] = capo_connect.types.subtypes.serialize_json(value["subtypes"])
    if "validation_test_types" in value:
        import capo_connect.types.validation_test_types

        out["ValidationTestTypes"] = (
            capo_connect.types.validation_test_types.serialize_json(
                value["validation_test_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> Filters:
    out: Filters = {}  # type: ignore[typeddict-item]
    if "Queues" in data:
        import capo_connect.types.queues

        out["queues"] = capo_connect.types.queues.deserialize_json(data["Queues"])
    if "Channels" in data:
        import capo_connect.types.channels

        out["channels"] = capo_connect.types.channels.deserialize_json(data["Channels"])
    if "RoutingProfiles" in data:
        import capo_connect.types.routing_profiles

        out["routing_profiles"] = capo_connect.types.routing_profiles.deserialize_json(
            data["RoutingProfiles"]
        )
    if "RoutingStepExpressions" in data:
        import capo_connect.types.routing_expressions

        out["routing_step_expressions"] = (
            capo_connect.types.routing_expressions.deserialize_json(
                data["RoutingStepExpressions"]
            )
        )
    if "AgentStatuses" in data:
        import capo_connect.types.agent_statuses

        out["agent_statuses"] = capo_connect.types.agent_statuses.deserialize_json(
            data["AgentStatuses"]
        )
    if "Subtypes" in data:
        import capo_connect.types.subtypes

        out["subtypes"] = capo_connect.types.subtypes.deserialize_json(data["Subtypes"])
    if "ValidationTestTypes" in data:
        import capo_connect.types.validation_test_types

        out["validation_test_types"] = (
            capo_connect.types.validation_test_types.deserialize_json(
                data["ValidationTestTypes"]
            )
        )
    return out
