"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListVectorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.index_arn
    import aws_sdk_s3vectors.types.index_name
    import aws_sdk_s3vectors.types.list_vectors_max_results
    import aws_sdk_s3vectors.types.list_vectors_next_token
    import aws_sdk_s3vectors.types.list_vectors_segment_count
    import aws_sdk_s3vectors.types.list_vectors_segment_index
    import aws_sdk_s3vectors.types.vector_bucket_name


class ListVectorsInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket. </p>"""
    index_name: NotRequired["aws_sdk_s3vectors.types.index_name.IndexName"]
    """<p>The name of the vector index.</p>"""
    index_arn: NotRequired["aws_sdk_s3vectors.types.index_arn.IndexArn"]
    """<p>The Amazon resource Name (ARN) of the vector index.</p>"""
    max_results: (
        "aws_sdk_s3vectors.types.list_vectors_max_results.ListVectorsMaxResults"
    )
    """<p>The maximum number of vectors to return on a page.</p> <p>If you don't specify <code>maxResults</code>, the <code>ListVectors</code> operation uses a default value of 500.</p> <p>If the processed dataset size exceeds 1 MB before reaching the <code>maxResults</code> value, the operation stops and returns the vectors that are retrieved up to that point, along with a <code>nextToken</code> that you can use in a subsequent request to retrieve the next set of results.</p>"""
    next_token: NotRequired[
        "aws_sdk_s3vectors.types.list_vectors_next_token.ListVectorsNextToken"
    ]
    """<p>Pagination token from a previous request. The value of this field is empty for an initial request.</p>"""
    segment_count: (
        "aws_sdk_s3vectors.types.list_vectors_segment_count.ListVectorsSegmentCount"
    )
    """<p>For a parallel <code>ListVectors</code> request, <code>segmentCount</code> represents the total number of vector segments into which the <code>ListVectors</code> operation will be divided. The value of <code>segmentCount</code> corresponds to the number of application workers that will perform the parallel <code>ListVectors</code> operation. For example, if you want to use four application threads to list vectors in a vector index, specify a <code>segmentCount</code> value of 4. </p> <p>If you specify a <code>segmentCount</code> value of 1, the <code>ListVectors</code> operation will be sequential rather than parallel.</p> <p>If you specify <code>segmentCount</code>, you must also specify <code>segmentIndex</code>.</p>"""
    segment_index: (
        "aws_sdk_s3vectors.types.list_vectors_segment_index.ListVectorsSegmentIndex"
    )
    """<p>For a parallel <code>ListVectors</code> request, <code>segmentIndex</code> is the index of the segment from which to list vectors in the current request. It identifies an individual segment to be listed by an application worker. </p> <p>Segment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to list vectors in a vector index, then the first thread specifies a <code>segmentIndex</code> value of 0, the second thread specifies 1, and so on. </p> <p>The value of <code>segmentIndex</code> must be less than the value provided for <code>segmentCount</code>. </p> <p>If you provide <code>segmentIndex</code>, you must also provide <code>segmentCount</code>.</p>"""
    return_data: "bool"
    """<p>If true, the vector data of each vector will be included in the response. The default value is <code>false</code>.</p>"""
    return_metadata: "bool"
    """<p>If true, the metadata associated with each vector will be included in the response. The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorsInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    out["maxResults"] = value.get("max_results", 500)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["segmentCount"] = value.get("segment_count", 1)
    out["segmentIndex"] = value.get("segment_index", 0)
    out["returnData"] = value.get("return_data", False)
    out["returnMetadata"] = value.get("return_metadata", False)
    return out


def deserialize_json(data: dict) -> ListVectorsInput:
    out: ListVectorsInput = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    if "indexArn" in data:
        out["index_arn"] = data["indexArn"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 500
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "segmentCount" in data:
        out["segment_count"] = data["segmentCount"]
    else:
        out["segment_count"] = 1
    if "segmentIndex" in data:
        out["segment_index"] = data["segmentIndex"]
    else:
        out["segment_index"] = 0
    if "returnData" in data:
        out["return_data"] = data["returnData"]
    else:
        out["return_data"] = False
    if "returnMetadata" in data:
        out["return_metadata"] = data["returnMetadata"]
    else:
        out["return_metadata"] = False
    return out
