"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseSearchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.string_condition
    import aws_sdk_connect.types.test_case_search_condition_list
    import aws_sdk_connect.types.test_case_status


class TestCaseSearchCriteria(TypedDict, closed=True):
    or_conditions: NotRequired[
        "aws_sdk_connect.types.test_case_search_condition_list.TestCaseSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an OR condition.</p>"""
    and_conditions: NotRequired[
        "aws_sdk_connect.types.test_case_search_condition_list.TestCaseSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an AND condition.</p>"""
    string_condition: NotRequired[
        "aws_sdk_connect.types.string_condition.StringCondition"
    ]
    """<p>A leaf node condition which can be used to specify a string condition.</p>"""
    status_condition: NotRequired[
        "aws_sdk_connect.types.test_case_status.TestCaseStatus"
    ]
    """<p>The status of the test case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import aws_sdk_connect.types.test_case_search_condition_list

        out["OrConditions"] = (
            aws_sdk_connect.types.test_case_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import aws_sdk_connect.types.test_case_search_condition_list

        out["AndConditions"] = (
            aws_sdk_connect.types.test_case_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import aws_sdk_connect.types.string_condition

        out["StringCondition"] = aws_sdk_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "status_condition" in value:
        import aws_sdk_connect.types.test_case_status

        out["StatusCondition"] = aws_sdk_connect.types.test_case_status.serialize_json(
            value["status_condition"]
        )
    return out


def deserialize_json(data: dict) -> TestCaseSearchCriteria:
    out: TestCaseSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import aws_sdk_connect.types.test_case_search_condition_list

        out["or_conditions"] = (
            aws_sdk_connect.types.test_case_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import aws_sdk_connect.types.test_case_search_condition_list

        out["and_conditions"] = (
            aws_sdk_connect.types.test_case_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "StringCondition" in data:
        import aws_sdk_connect.types.string_condition

        out["string_condition"] = (
            aws_sdk_connect.types.string_condition.deserialize_json(
                data["StringCondition"]
            )
        )
    if "StatusCondition" in data:
        import aws_sdk_connect.types.test_case_status

        out["status_condition"] = (
            aws_sdk_connect.types.test_case_status.deserialize_json(
                data["StatusCondition"]
            )
        )
    return out
