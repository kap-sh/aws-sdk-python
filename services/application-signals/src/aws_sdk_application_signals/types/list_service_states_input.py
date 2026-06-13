"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceStatesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.attribute_filters
    import aws_sdk_application_signals.types.aws_account_id
    import aws_sdk_application_signals.types.list_service_states_max_results
    import aws_sdk_application_signals.types.next_token


class ListServiceStatesInput(TypedDict):
    start_time: "datetime.datetime"
    """<p>The start of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>"""
    max_results: "aws_sdk_application_signals.types.list_service_states_max_results.ListServiceStatesMaxResults"
    """<p>The maximum number of service states to return in one operation. If you omit this parameter, the default of 20 is used.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of service states.</p>"""
    include_linked_accounts: "bool"
    """<p>If you are using this operation in a monitoring account, specify <code>true</code> to include service states from source accounts in the returned data.</p>"""
    aws_account_id: NotRequired[
        "aws_sdk_application_signals.types.aws_account_id.AwsAccountId"
    ]
    """<p>The Amazon Web Services account ID to filter service states by. Use this to limit results to services from a specific account.</p>"""
    attribute_filters: NotRequired[
        "aws_sdk_application_signals.types.attribute_filters.AttributeFilters"
    ]
    """<p>A list of attribute filters to narrow down the services. You can filter by platform, environment, or other service attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceStatesInput) -> dict:
    out: dict = {}
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
    out["MaxResults"] = value.get("max_results", 20)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["IncludeLinkedAccounts"] = value.get("include_linked_accounts", False)
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "attribute_filters" in value:
        import aws_sdk_application_signals.types.attribute_filters

        out["AttributeFilters"] = (
            aws_sdk_application_signals.types.attribute_filters.serialize_json(
                value["attribute_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListServiceStatesInput:
    out: ListServiceStatesInput = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceStatesInput.start_time required")
    if "EndTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("ListServiceStatesInput.end_time required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 20
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "IncludeLinkedAccounts" in data:
        out["include_linked_accounts"] = data["IncludeLinkedAccounts"]
    else:
        out["include_linked_accounts"] = False
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    if "AttributeFilters" in data:
        import aws_sdk_application_signals.types.attribute_filters

        out["attribute_filters"] = (
            aws_sdk_application_signals.types.attribute_filters.deserialize_json(
                data["AttributeFilters"]
            )
        )
    return out
