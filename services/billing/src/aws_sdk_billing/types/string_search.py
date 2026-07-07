"""Generated from Smithy shape ``com.amazonaws.billing#StringSearch``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.search_option
    import aws_sdk_billing.types.search_value


class StringSearch(TypedDict, closed=True):
    search_option: "aws_sdk_billing.types.search_option.SearchOption"
    """<p> The type of search operation to perform on the string value. Determines how the search value is matched against the target field. </p>"""
    search_value: "aws_sdk_billing.types.search_value.SearchValue"
    """<p> The string value to use in the search operation. This value is compared against the target field using the specified search option. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringSearch) -> dict:
    out: dict = {}
    import aws_sdk_billing.types.search_option

    out["searchOption"] = aws_sdk_billing.types.search_option.serialize_aws_json_1_0(
        value["search_option"]
    )
    out["searchValue"] = value["search_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StringSearch:
    out: StringSearch = {}  # type: ignore[typeddict-item]
    if "searchOption" in data:
        import aws_sdk_billing.types.search_option

        out["search_option"] = (
            aws_sdk_billing.types.search_option.deserialize_aws_json_1_0(
                data["searchOption"]
            )
        )
    else:
        raise DeserializationError("StringSearch.search_option required")
    if "searchValue" in data:
        out["search_value"] = data["searchValue"]
    else:
        raise DeserializationError("StringSearch.search_value required")
    return out
