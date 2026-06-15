"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListEntityEventsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.attributes
    import aws_sdk_application_signals.types.list_entity_events_max_results
    import aws_sdk_application_signals.types.next_token


class ListEntityEventsInput(TypedDict):
    entity: "aws_sdk_application_signals.types.attributes.Attributes"
    r"""<p>The entity for which to retrieve change events. This specifies the service, resource, or other entity whose event history you want to examine.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> <li> <p> <code>AwsAccountId</code> specifies the account where this object is in.</p> </li> </ul> <p>Below is an example of a service.</p> <p> <code>{ \"Type\": \"Service\", \"Name\": \"visits-service\", \"Environment\": \"petclinic-test\" }</code> </p> <p>Below is an example of a resource.</p> <p> <code>{ \"Type\": \"AWS::Resource\", \"ResourceType\": \"AWS::DynamoDB::Table\", \"Identifier\": \"Customers\" }</code> </p>"""
    start_time: "datetime.datetime"
    """<p>The start of the time period to retrieve change events for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: <code>1698778057</code> </p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period to retrieve change events for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: <code>1698778057</code> </p>"""
    max_results: "aws_sdk_application_signals.types.list_entity_events_max_results.ListEntityEventsMaxResults"
    """<p>The maximum number of change events to return in one operation. If you omit this parameter, the default of 50 is used.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of change events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntityEventsInput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.attributes

    out["Entity"] = aws_sdk_application_signals.types.attributes.serialize_json(
        value["entity"]
    )
    import aws_sdk_application_signals.types._prelude.timestamp

    out["StartTime"] = (
        aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    )
    import aws_sdk_application_signals.types._prelude.timestamp

    out["EndTime"] = (
        aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListEntityEventsInput:
    out: ListEntityEventsInput = {}  # type: ignore[typeddict-item]
    if "Entity" in data:
        import aws_sdk_application_signals.types.attributes

        out["entity"] = aws_sdk_application_signals.types.attributes.deserialize_json(
            data["Entity"]
        )
    else:
        raise DeserializationError("ListEntityEventsInput.entity required")
    if "StartTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ListEntityEventsInput.start_time required")
    if "EndTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("ListEntityEventsInput.end_time required")
    return out
