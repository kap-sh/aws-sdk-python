"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SearchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.cursor
    import aws_sdk_cloudsearch_domain.types.expr
    import aws_sdk_cloudsearch_domain.types.facet
    import aws_sdk_cloudsearch_domain.types.filter_query
    import aws_sdk_cloudsearch_domain.types.highlight
    import aws_sdk_cloudsearch_domain.types.partial
    import aws_sdk_cloudsearch_domain.types.query
    import aws_sdk_cloudsearch_domain.types.query_options
    import aws_sdk_cloudsearch_domain.types.query_parser
    import aws_sdk_cloudsearch_domain.types.return_
    import aws_sdk_cloudsearch_domain.types.size
    import aws_sdk_cloudsearch_domain.types.sort
    import aws_sdk_cloudsearch_domain.types.start
    import aws_sdk_cloudsearch_domain.types.stat

SearchRequest = TypedDict(
    "SearchRequest",
    {
        "cursor": NotRequired["aws_sdk_cloudsearch_domain.types.cursor.Cursor"],
        "expr": NotRequired["aws_sdk_cloudsearch_domain.types.expr.Expr"],
        "facet": NotRequired["aws_sdk_cloudsearch_domain.types.facet.Facet"],
        "filter_query": NotRequired[
            "aws_sdk_cloudsearch_domain.types.filter_query.FilterQuery"
        ],
        "highlight": NotRequired[
            "aws_sdk_cloudsearch_domain.types.highlight.Highlight"
        ],
        "partial": "aws_sdk_cloudsearch_domain.types.partial.Partial",
        "query": "aws_sdk_cloudsearch_domain.types.query.Query",
        "query_options": NotRequired[
            "aws_sdk_cloudsearch_domain.types.query_options.QueryOptions"
        ],
        "query_parser": NotRequired[
            "aws_sdk_cloudsearch_domain.types.query_parser.QueryParser"
        ],
        "return": NotRequired["aws_sdk_cloudsearch_domain.types.return_.Return"],
        "size": "aws_sdk_cloudsearch_domain.types.size.Size",
        "sort": NotRequired["aws_sdk_cloudsearch_domain.types.sort.Sort"],
        "start": "aws_sdk_cloudsearch_domain.types.start.Start",
        "stats": NotRequired["aws_sdk_cloudsearch_domain.types.stat.Stat"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SearchRequest:
    out: SearchRequest = {}  # type: ignore[typeddict-item]
    return out
