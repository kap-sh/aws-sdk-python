"""Generated from Smithy shape ``com.amazonaws.cloudsearch#OptionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

"""<p>The state of processing a change to an option. One of:</p> <ul> <li>RequiresIndexDocuments: The option's latest value will not be deployed until <a>IndexDocuments</a> has been called and indexing is complete.</li> <li>Processing: The option's latest value is in the process of being activated.</li> <li>Active: The option's latest value is fully deployed. </li> <li>FailedToValidate: The option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.</li> </ul>"""
OptionState: TypeAlias = Literal[
    "RequiresIndexDocuments",
    "Processing",
    "Active",
    "FailedToValidate",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RequiresIndexDocuments",
        "Processing",
        "Active",
        "FailedToValidate",
    )
)


def to_query_text(value: OptionState) -> str:
    return value


def from_query_text(text: str) -> OptionState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OptionState value: {text!r}")
    return cast(OptionState, text)


def serialize_query(
    value: OptionState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OptionState:
    return from_query_text(el.text or "")
