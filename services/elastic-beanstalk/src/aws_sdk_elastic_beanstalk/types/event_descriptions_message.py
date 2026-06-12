"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EventDescriptionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.event_description_list
    import aws_sdk_elastic_beanstalk.types.token


class EventDescriptionsMessage(TypedDict):
    events: NotRequired[
        "aws_sdk_elastic_beanstalk.types.event_description_list.EventDescriptionList"
    ]
    """<p> A list of <a>EventDescription</a>. </p>"""
    next_token: NotRequired["aws_sdk_elastic_beanstalk.types.token.Token"]
    """<p> If returned, this indicates that there are more results to obtain. Use this token in the next <a>DescribeEvents</a> call to get the next batch of events. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventDescriptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "events" in value:
        import aws_sdk_elastic_beanstalk.types.event_description_list

        aws_sdk_elastic_beanstalk.types.event_description_list.serialize_query(
            value["events"], pairs, f"{prefix}.Events"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> EventDescriptionsMessage:
    out: EventDescriptionsMessage = {}  # type: ignore[typeddict-item]
    child_events = el.find("Events")
    if child_events is not None:
        import aws_sdk_elastic_beanstalk.types.event_description_list

        out["events"] = (
            aws_sdk_elastic_beanstalk.types.event_description_list.deserialize_query(
                child_events
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
