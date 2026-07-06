"""Generated from Smithy shape ``com.amazonaws.ecr#SigningRepositoryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.signing_repository_filter_type
    import aws_sdk_ecr.types.signing_repository_filter_value


class SigningRepositoryFilter(TypedDict, closed=True):
    filter: (
        "aws_sdk_ecr.types.signing_repository_filter_value.SigningRepositoryFilterValue"
    )
    """<p>The filter value used to match repository names. When using <code>WILDCARD_MATCH</code>, the <code>*</code> character matches any sequence of characters.</p> <p>Examples:</p> <ul> <li> <p> <code>myapp/*</code> - Matches all repositories starting with <code>myapp/</code> </p> </li> <li> <p> <code>*/production</code> - Matches all repositories ending with <code>/production</code> </p> </li> <li> <p> <code>*prod*</code> - Matches all repositories containing <code>prod</code> </p> </li> </ul>"""
    filter_type: (
        "aws_sdk_ecr.types.signing_repository_filter_type.SigningRepositoryFilterType"
    )
    """<p>The type of filter to apply. Currently, only <code>WILDCARD_MATCH</code> is supported, which uses wildcard patterns to match repository names.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningRepositoryFilter) -> dict:
    out: dict = {}
    out["filter"] = value["filter"]
    import aws_sdk_ecr.types.signing_repository_filter_type

    out["filterType"] = (
        aws_sdk_ecr.types.signing_repository_filter_type.serialize_aws_json_1_1(
            value["filter_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SigningRepositoryFilter:
    out: SigningRepositoryFilter = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        out["filter"] = data["filter"]
    else:
        raise DeserializationError("SigningRepositoryFilter.filter required")
    if "filterType" in data:
        import aws_sdk_ecr.types.signing_repository_filter_type

        out["filter_type"] = (
            aws_sdk_ecr.types.signing_repository_filter_type.deserialize_aws_json_1_1(
                data["filterType"]
            )
        )
    else:
        raise DeserializationError("SigningRepositoryFilter.filter_type required")
    return out
