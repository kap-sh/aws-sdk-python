"""Generated from Smithy shape ``com.amazonaws.mq#ListUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__integer_min5_max100
    import aws_sdk_mq.types.__list_of_user_summary
    import aws_sdk_mq.types.__string


class ListUsersResponse(TypedDict, closed=True):
    broker_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Required. The unique ID that Amazon MQ generates for the broker.</p>"""
    max_results: NotRequired[
        "aws_sdk_mq.types.__integer_min5_max100.__integerMin5Max100"
    ]
    """<p>Required. The maximum number of ActiveMQ users that can be returned per page (20 by default). This value must be an integer from 5 to 100.</p>"""
    next_token: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p>"""
    users: NotRequired["aws_sdk_mq.types.__list_of_user_summary.__listOfUserSummary"]
    """<p>Required. The list of all ActiveMQ usernames for the specified broker. Does not apply to RabbitMQ brokers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "users" in value:
        import aws_sdk_mq.types.__list_of_user_summary

        out["users"] = aws_sdk_mq.types.__list_of_user_summary.serialize_json(
            value["users"]
        )
    return out


def deserialize_json(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if "brokerId" in data:
        out["broker_id"] = data["brokerId"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "users" in data:
        import aws_sdk_mq.types.__list_of_user_summary

        out["users"] = aws_sdk_mq.types.__list_of_user_summary.deserialize_json(
            data["users"]
        )
    return out
